%global packname  LPCM
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.44.5
Release:          1%{?dist}
Summary:          Local principal curve methods

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.44-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Fitting multivariate data patterns with local principal curves; including
simple tools for data compression (projection), bandwidth selection, and
measuring goodness-of-fit.

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
%doc %{rlibdir}/LPCM/DESCRIPTION
%doc %{rlibdir}/LPCM/html
%{rlibdir}/LPCM/INDEX
%{rlibdir}/LPCM/help
%{rlibdir}/LPCM/data
%{rlibdir}/LPCM/Meta
%{rlibdir}/LPCM/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.44.5-1
- initial package for Fedora