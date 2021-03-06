%global packname  GMD
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2
Release:          1%{?dist}
Summary:          Generalized Minimum Distance of distributions

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-tools 

BuildRequires:    R-devel tex(latex) R-tools 

%description
GMD is a package for non-parametric distance measurement between two
discrete frequency distributions.

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
%doc %{rlibdir}/GMD/CITATION
%doc %{rlibdir}/GMD/DESCRIPTION
%doc %{rlibdir}/GMD/doc
%doc %{rlibdir}/GMD/html
%{rlibdir}/GMD/help
%{rlibdir}/GMD/R
%{rlibdir}/GMD/demo
%{rlibdir}/GMD/data
%{rlibdir}/GMD/INDEX
%{rlibdir}/GMD/NAMESPACE
%{rlibdir}/GMD/Meta
%{rlibdir}/GMD/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2-1
- initial package for Fedora