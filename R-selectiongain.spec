%global packname  selectiongain
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.7.0
Release:          1%{?dist}
Summary:          Expected gain from multistages selection

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-mvtnorm 

BuildRequires:    R-devel tex(latex) R-mvtnorm 

%description
This package calculate the gain from selection, which is described by
Cochran (1951). For one-stage selection the gain is defined as \eqn{\Delta
G (y) = i \rho_{y} \rho_{1}}, where \eqn{i} is the selection intensity,
\eqn{\rho_{1}} is the correlation between the true breeding value and the
selection index \eqn{y} (Utz1969). The numerical calculation is based on
Tallis' algorithm (Tallis1961).

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
%doc %{rlibdir}/selectiongain/DESCRIPTION
%doc %{rlibdir}/selectiongain/html
%{rlibdir}/selectiongain/Meta
%{rlibdir}/selectiongain/help
%{rlibdir}/selectiongain/INDEX
%{rlibdir}/selectiongain/R
%{rlibdir}/selectiongain/LICENSE

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.7.0-1
- initial package for Fedora