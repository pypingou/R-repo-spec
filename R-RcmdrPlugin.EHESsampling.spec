%global packname  RcmdrPlugin.EHESsampling
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.0
Release:          1%{?dist}
Summary:          Tools for sampling in European Health Examination Surveys (EHES)

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Rcmdr R-lpSolve R-sampling R-MASS R-tcltk2 R-Hmisc 


BuildRequires:    R-devel tex(latex) R-Rcmdr R-lpSolve R-sampling R-MASS R-tcltk2 R-Hmisc



%description
This package includes tools useful for European Health Examination
Surveys. This includes selecting a two-stage sample and creating and
checking encoded serial numbers. The EHES Pilot project has received
funding from the European Commission and DG Sanco. The views expressed
here are those of the authors and they do not represent Commission's
official position.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0-1
- initial package for Fedora