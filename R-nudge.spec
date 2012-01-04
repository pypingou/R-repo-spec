%global packname  nudge
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.20.0
Release:          1%{?dist}
Summary:          Normal Uniform Differential Gene Expression detection

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Package for normalizing microarray data in single and multiple replicate
experiments and fitting a normal-uniform mixture to detect differentially
expressed genes in the cases where the two samples are being compared
directly or indirectly (via a common reference sample)

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{rlibdir}/nudge/html
%doc %{rlibdir}/nudge/DESCRIPTION
%doc %{rlibdir}/nudge/doc
%{rlibdir}/nudge/NAMESPACE
%{rlibdir}/nudge/R
%{rlibdir}/nudge/INDEX
%{rlibdir}/nudge/help
%{rlibdir}/nudge/data
%{rlibdir}/nudge/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.20.0-1
- initial package for Fedora