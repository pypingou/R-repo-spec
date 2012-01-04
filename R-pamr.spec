%global packname  pamr
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.51.0
Release:          1%{?dist}
Summary:          Pam: prediction analysis for microarrays

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-cluster R-survival 

BuildRequires:    R-devel tex(latex) R-cluster R-survival 

%description
Some functions for sample classification in microarrays

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
%doc %{rlibdir}/pamr/html
%doc %{rlibdir}/pamr/DESCRIPTION
%doc %{rlibdir}/pamr/doc
%{rlibdir}/pamr/data
%{rlibdir}/pamr/R
%{rlibdir}/pamr/NAMESPACE
%{rlibdir}/pamr/INDEX
%{rlibdir}/pamr/help
%{rlibdir}/pamr/libs
%{rlibdir}/pamr/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.51.0-1
- initial package for Fedora