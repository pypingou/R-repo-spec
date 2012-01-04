%global packname  gridSVG
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.8.1
Release:          1%{?dist}
Summary:          Export grid graphics as SVG

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.8-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-grid 

BuildRequires:    R-devel tex(latex) R-methods R-grid 

%description
Export grid graphics as SVG

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
%doc %{rlibdir}/gridSVG/doc
%doc %{rlibdir}/gridSVG/html
%doc %{rlibdir}/gridSVG/DESCRIPTION
%{rlibdir}/gridSVG/Meta
%{rlibdir}/gridSVG/INDEX
%{rlibdir}/gridSVG/R
%{rlibdir}/gridSVG/NAMESPACE
%{rlibdir}/gridSVG/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8.1-1
- initial package for Fedora