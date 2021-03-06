%global packname  hts
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.02
Release:          1%{?dist}
Summary:          Hierarchical and grouped time series

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-forecast R-SparseM 

BuildRequires:    R-devel tex(latex) R-forecast R-SparseM 

%description
Methods for analysing and forecasting hierarchical and grouped time

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
%doc %{rlibdir}/hts/html
%doc %{rlibdir}/hts/DESCRIPTION
%{rlibdir}/hts/help
%{rlibdir}/hts/INDEX
%{rlibdir}/hts/Meta
%{rlibdir}/hts/NAMESPACE
%{rlibdir}/hts/data
%{rlibdir}/hts/R

%changelog
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.02-1
- initial package for Fedora