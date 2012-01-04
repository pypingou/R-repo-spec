%global packname  isa2
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.3.1
Release:          1%{?dist}
Summary:          The Iterative Signature Algorithm

Group:            Applications/Engineering 
License:          file LICENCE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
The ISA is a biclustering algorithm that finds modules in an input matrix.
A module or bicluster is a block of the reordered input matrix.

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
%doc %{rlibdir}/isa2/CITATION
%doc %{rlibdir}/isa2/doc
%doc %{rlibdir}/isa2/LICENCE
%doc %{rlibdir}/isa2/html
%doc %{rlibdir}/isa2/DESCRIPTION
%{rlibdir}/isa2/help
%{rlibdir}/isa2/Meta
%{rlibdir}/isa2/libs
%{rlibdir}/isa2/R
%{rlibdir}/isa2/NAMESPACE
%{rlibdir}/isa2/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.1-1
- initial package for Fedora