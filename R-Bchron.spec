%global packname  Bchron
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          3.1.4
Release:          1%{?dist}
Summary:          Bayesian chronologies via compound Poisson-Gamma processes.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-hdrcde R-coda R-svDialogs 


BuildRequires:    R-devel tex(latex) R-hdrcde R-coda R-svDialogs



%description
This package takes dating information to produce joint chronological
reconstructions for age-depth data. The package allows for: radiocarbon
and non-radiocarbon depths, thickness errors, outlying dates, multiple
calibration curves, and event prediction. It also produces some pretty
pictures, and writes all output to files to allow for further analysis (eg
palaeoclimate reconstruction). There is a menu system for users, as well
as a command line interface for advanced and/or batch processing. This
version contains an update to produce better plots of proxy data via the
function Bchronproxyplot. ***IMPORTANT NOTE*** This version fixes a
serious bug which was present in versions 3.1.1 and 3.1.2. You should have
noticed this bug anyway when you ran the Bchronconvergecheck function.

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
%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.1.4-1
- initial package for Fedora