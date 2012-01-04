%global packname  EQL
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Extended-Quasi-Likelihood-Function (EQL)

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-ttutils 

BuildRequires:    R-devel tex(latex) R-ttutils 

%description
Computation of the EQL for a given family of variance functions,
Saddlepoint-approximations and related auxiliary functions (e.g. Hermite

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
%doc %{rlibdir}/EQL/html
%doc %{rlibdir}/EQL/CITATION
%doc %{rlibdir}/EQL/DESCRIPTION
%{rlibdir}/EQL/Meta
%{rlibdir}/EQL/INDEX
%{rlibdir}/EQL/R
%{rlibdir}/EQL/NAMESPACE
%{rlibdir}/EQL/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora