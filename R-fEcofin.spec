%global packname  fEcofin
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          290.76
Release:          1%{?dist}
Summary:          Economic and Financial Data Sets

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-utils 

BuildRequires:    R-devel tex(latex) R-utils 

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
%doc %{rlibdir}/fEcofin/html
%doc %{rlibdir}/fEcofin/DESCRIPTION
%{rlibdir}/fEcofin/unitTests
%{rlibdir}/fEcofin/DocCopying.pdf
%{rlibdir}/fEcofin/Meta
%{rlibdir}/fEcofin/INDEX
%{rlibdir}/fEcofin/R
%{rlibdir}/fEcofin/COPYRIGHT.html
%{rlibdir}/fEcofin/help
%{rlibdir}/fEcofin/data
%{rlibdir}/fEcofin/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 290.76-1
- initial package for Fedora