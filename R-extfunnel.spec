%global packname  extfunnel
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Additional Funnel Plot Augmentations

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-rmeta 

BuildRequires:    R-devel tex(latex) R-rmeta 

%description
This is a package containing the function extfunnel() which produces a
funnel plot including additional augmentations such as statistical
significance contours and heterogeneity contours.

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
%doc %{rlibdir}/extfunnel/html
%doc %{rlibdir}/extfunnel/DESCRIPTION
%{rlibdir}/extfunnel/R
%{rlibdir}/extfunnel/Meta
%{rlibdir}/extfunnel/help
%{rlibdir}/extfunnel/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2-1
- initial package for Fedora