%global packname  pear
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Package for Periodic Autoregression Analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Package for estimating periodic autoregressive models. Datasets: monthly
ozone and Fraser riverflow. Plots: periodic versions of boxplot,
auto/partial correlations, moving-average expansion.

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
%doc %{rlibdir}/pear/NEWS
%doc %{rlibdir}/pear/CITATION
%doc %{rlibdir}/pear/html
%doc %{rlibdir}/pear/DESCRIPTION
%doc %{rlibdir}/pear/doc
%{rlibdir}/pear/data
%{rlibdir}/pear/R
%{rlibdir}/pear/NAMESPACE
%{rlibdir}/pear/INDEX
%{rlibdir}/pear/help
%{rlibdir}/pear/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2-1
- initial package for Fedora