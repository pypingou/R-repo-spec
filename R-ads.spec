%global packname  ads
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.10
Release:          1%{?dist}
Summary:          Spatial point patterns analysis

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-10.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Perform first- and second-order multi-scale analyses derived from Ripley's
K-function, for univariate, multivariate and marked mapped data in
rectangular, circular or irregular shaped sampling windows, with test of
statitical significance based on Monte Carlo simulations.

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
* Fri Nov 25 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.10-1
- initial package for Fedora