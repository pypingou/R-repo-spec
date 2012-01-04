%global packname  VisCov
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Visualizing of distributions of covariance matrices

Group:            Applications/Engineering 
License:          file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-bayesm R-MASS R-clusterGeneration R-TeachingDemos R-scatterplot3d R-KernSmooth 

BuildRequires:    R-devel tex(latex) R-bayesm R-MASS R-clusterGeneration R-TeachingDemos R-scatterplot3d R-KernSmooth 

%description
Visualizing of distributions of covariance matrices

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
%doc %{rlibdir}/VisCov/html
%doc %{rlibdir}/VisCov/DESCRIPTION
%{rlibdir}/VisCov/LICENSE
%{rlibdir}/VisCov/NAMESPACE
%{rlibdir}/VisCov/Meta
%{rlibdir}/VisCov/help
%{rlibdir}/VisCov/INDEX
%{rlibdir}/VisCov/R

%changelog
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora