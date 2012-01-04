%global packname  RAD
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2
Release:          1%{?dist}
Summary:          Fit RAD models to biological data

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-mvtnorm R-MASS 

BuildRequires:    R-devel tex(latex) R-mvtnorm R-MASS 

%description
Fit a variety of models to Rank Abundance Data

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
%doc %{rlibdir}/RAD/DESCRIPTION
%doc %{rlibdir}/RAD/html
%{rlibdir}/RAD/NAMESPACE
%{rlibdir}/RAD/INDEX
%{rlibdir}/RAD/R
%{rlibdir}/RAD/help
%{rlibdir}/RAD/libs
%{rlibdir}/RAD/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2-1
- initial package for Fedora