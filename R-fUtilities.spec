%global packname  fUtilities
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2110.78
Release:          1%{?dist}
Summary:          Function Utilities

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-MASS 

BuildRequires:    R-devel tex(latex) R-methods R-MASS 

%description
Environment for teaching "Financial Engineering and Computational Finance"

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
%doc %{rlibdir}/fUtilities/DESCRIPTION
%doc %{rlibdir}/fUtilities/html
%{rlibdir}/fUtilities/Meta
%{rlibdir}/fUtilities/NAMESPACE
%{rlibdir}/fUtilities/COPYRIGHT.html
%{rlibdir}/fUtilities/DocCopying.pdf
%{rlibdir}/fUtilities/R
%{rlibdir}/fUtilities/INDEX
%{rlibdir}/fUtilities/help
%{rlibdir}/fUtilities/unitTests

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2110.78-1
- initial package for Fedora