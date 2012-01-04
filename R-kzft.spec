%global packname  kzft
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.17
Release:          1%{?dist}
Summary:          Kolmogorov-Zurbenko Fourier Transform and Applications

Group:            Applications/Engineering 
License:          GPL Version 2 or later
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-polynom 

BuildRequires:    R-devel tex(latex) R-polynom 

%description
A colletion of functions to implement Kolmogorov-Zurbenko Fourier
transform based periodograms and smoothing methods

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
%doc %{rlibdir}/kzft/html
%doc %{rlibdir}/kzft/DESCRIPTION
%{rlibdir}/kzft/help
%{rlibdir}/kzft/Meta
%{rlibdir}/kzft/INDEX
%{rlibdir}/kzft/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.17-1
- initial package for Fedora