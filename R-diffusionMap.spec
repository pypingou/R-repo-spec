%global packname  diffusionMap
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Diffusion map

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-scatterplot3d R-igraph R-Matrix 

BuildRequires:    R-devel tex(latex) R-scatterplot3d R-igraph R-Matrix 

%description
Implements diffusion map method of data parametrization, including
creation and visualization of diffusion map, clustering with diffusion
K-means and regression using adaptive regression model.

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
%doc %{rlibdir}/diffusionMap/html
%doc %{rlibdir}/diffusionMap/DESCRIPTION
%{rlibdir}/diffusionMap/data
%{rlibdir}/diffusionMap/NAMESPACE
%{rlibdir}/diffusionMap/R
%{rlibdir}/diffusionMap/help
%{rlibdir}/diffusionMap/Meta
%{rlibdir}/diffusionMap/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora