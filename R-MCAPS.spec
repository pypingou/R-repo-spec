%global packname  MCAPS
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.3.1
Release:          1%{?dist}
Summary:          MCAPS data and results

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stashR 


BuildRequires:    R-devel tex(latex) R-stashR



%description
Weather and air pollution data, risk estimates, and other information from
the Medicare Air Pollution Study (MCAPS) of 204 U.S. counties, 1999--2002

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
%doc %{rlibdir}/MCAPS/CITATION
%doc %{rlibdir}/MCAPS/COPYING
%doc %{rlibdir}/MCAPS/html
%doc %{rlibdir}/MCAPS/DESCRIPTION
%{rlibdir}/MCAPS/R
%{rlibdir}/MCAPS/misc-code
%{rlibdir}/MCAPS/NAMESPACE
%{rlibdir}/MCAPS/help
%{rlibdir}/MCAPS/INDEX
%{rlibdir}/MCAPS/Meta

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.1-1
- initial package for Fedora