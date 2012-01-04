%global packname  Rvelslant
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2.3
Release:          1%{?dist}
Summary:          Downhole Seismic Analysis in R

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS 

BuildRequires:    R-devel tex(latex) R-MASS 

%description
R scripts for interactively analyzing downhole seismic data and
interpreting layered velocity models of constant velocity layers
accounting for refractions across layer boundaries.

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
%doc %{rlibdir}/Rvelslant/DESCRIPTION
%doc %{rlibdir}/Rvelslant/html
%{rlibdir}/Rvelslant/data
%{rlibdir}/Rvelslant/R
%{rlibdir}/Rvelslant/Meta
%{rlibdir}/Rvelslant/help
%{rlibdir}/Rvelslant/NAMESPACE
%{rlibdir}/Rvelslant/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.3-1
- initial package for Fedora