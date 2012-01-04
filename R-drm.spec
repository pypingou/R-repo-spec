%global packname  drm
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.5.8
Release:          1%{?dist}
Summary:          Regression and association models for repeated categorical data

Group:            Applications/Engineering 
License:          GPL (>=2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.5-8.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Likelihood-based marginal regression and association modelling for
repeated, or otherwise clustered, categorical responses using dependence
ratio as a measure of the association

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
%doc %{rlibdir}/drm/DESCRIPTION
%doc %{rlibdir}/drm/html
%{rlibdir}/drm/help
%{rlibdir}/drm/INDEX
%{rlibdir}/drm/Meta
%{rlibdir}/drm/NAMESPACE
%{rlibdir}/drm/data
%{rlibdir}/drm/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.8-1
- initial package for Fedora