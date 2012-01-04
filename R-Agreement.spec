%global packname  Agreement
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.8.1
Release:          1%{?dist}
Summary:          Statistical Tools for Measuring Agreement

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.8-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-R2HTML 

BuildRequires:    R-devel tex(latex) R-R2HTML 

%description
This package computes several statistics for measuring agreement, for
example, mean square deviation (MSD), total deviation index (TDI) or
concordance correlation coefficient (CCC). It can be used for both
continuous data and categorical data for multiple raters and multiple
readings cases.

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
%doc %{rlibdir}/Agreement/DESCRIPTION
%doc %{rlibdir}/Agreement/html
%{rlibdir}/Agreement/INDEX
%{rlibdir}/Agreement/data
%{rlibdir}/Agreement/help
%{rlibdir}/Agreement/R
%{rlibdir}/Agreement/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8.1-1
- initial package for Fedora