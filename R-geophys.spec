%global packname  geophys
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2.1
Release:          1%{?dist}
Summary:          Geophysics, Continuum Mechanics, Mogi Model

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-RPMG R-RFOC R-MASS R-cluster R-stats 

BuildRequires:    R-devel tex(latex) R-RPMG R-RFOC R-MASS R-cluster R-stats 

%description
Geophysics, Continuum Mechanics, Mogi Model, Okada Model

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
%doc %{rlibdir}/geophys/DESCRIPTION
%doc %{rlibdir}/geophys/html
%{rlibdir}/geophys/R
%{rlibdir}/geophys/help
%{rlibdir}/geophys/INDEX
%{rlibdir}/geophys/NAMESPACE
%{rlibdir}/geophys/demo
%{rlibdir}/geophys/data
%{rlibdir}/geophys/Meta

%changelog
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.1-1
- initial package for Fedora