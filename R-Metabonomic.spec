%global packname  Metabonomic
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          3.5
Release:          1%{?dist}
Summary:          GUI for Metabonomic Analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-tcltk R-tkrplot R-robustbase R-MASS R-gpls R-pls R-splines R-class R-nnet R-AMORE R-clusterSim R-hddplot R-scatterplot3d R-relimp R-Icens R-FTICRMS R-waved R-Matrix R-caTools 


BuildRequires:    R-devel tex(latex) R-tcltk R-tkrplot R-robustbase R-MASS R-gpls R-pls R-splines R-class R-nnet R-AMORE R-clusterSim R-hddplot R-scatterplot3d R-relimp R-Icens R-FTICRMS R-waved R-Matrix R-caTools



%description
Graphical User Interface for the Metabonomic Analysis (Baseline,
Normalization, Peak Detection, PCA, PLS, Nearest Neigbourgt, Neural
Network) developed to make easy this data analysis.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.5-1
- initial package for Fedora