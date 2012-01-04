%global packname  voronoi
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Methods and applications related to Voronoi tessellations

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-deldir R-spatialkernel R-splancs R-gpclib 

BuildRequires:    R-devel tex(latex) R-deldir R-spatialkernel R-splancs R-gpclib 

%description
Methods and applications related to Voronoi tessellations

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
%doc %{rlibdir}/voronoi/html
%doc %{rlibdir}/voronoi/DESCRIPTION
%{rlibdir}/voronoi/INDEX
%{rlibdir}/voronoi/R
%{rlibdir}/voronoi/NAMESPACE
%{rlibdir}/voronoi/help
%{rlibdir}/voronoi/Meta

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora