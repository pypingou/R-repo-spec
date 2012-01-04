%global packname  fractaldim
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.8.1
Release:          1%{?dist}
Summary:          Estimation of fractal dimensions

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.8-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-abind 

BuildRequires:    R-devel tex(latex) R-abind 

%description
Implements various methods for estimating fractal dimension of time series
and 2-dimensional data.

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
%doc %{rlibdir}/fractaldim/html
%doc %{rlibdir}/fractaldim/DESCRIPTION
%{rlibdir}/fractaldim/NAMESPACE
%{rlibdir}/fractaldim/help
%{rlibdir}/fractaldim/R
%{rlibdir}/fractaldim/INDEX
%{rlibdir}/fractaldim/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8.1-1
- initial package for Fedora