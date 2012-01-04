%global packname  CRTSize
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2
Release:          1%{?dist}
Summary:          Sample Size Estimation Functions for Cluster Randomized Trials

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package contains basic tools for the purpose of sample size
estimation in cluster (group) randomized trials. The package contains
traditional power-based methods, empirical smoothing (Rotondi and Donner,
2009), and updated meta-analysis techniques (Rotondi and Donner, 2011).

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
%doc %{rlibdir}/CRTSize/DESCRIPTION
%doc %{rlibdir}/CRTSize/html
%{rlibdir}/CRTSize/Meta
%{rlibdir}/CRTSize/INDEX
%{rlibdir}/CRTSize/R
%{rlibdir}/CRTSize/NAMESPACE
%{rlibdir}/CRTSize/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2-1
- initial package for Fedora