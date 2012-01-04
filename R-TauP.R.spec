%global packname  TauP.R
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Earthquake Traveltime Calculations for 1-D Earth Models

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Evaluates traveltimes and ray paths using predefined Earth (or other
planet) models.  Includes phase plotting routines. The IASP91 and AK135
Earth models are included, and most important arrival phases can be

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
%doc %{rlibdir}/TauP.R/DESCRIPTION
%doc %{rlibdir}/TauP.R/html
%{rlibdir}/TauP.R/R
%{rlibdir}/TauP.R/INDEX
%{rlibdir}/TauP.R/data
%{rlibdir}/TauP.R/NAMESPACE
RPM build errors:
%{rlibdir}/TauP.R/Meta
%{rlibdir}/TauP.R/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora