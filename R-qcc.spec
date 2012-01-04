%global packname  qcc
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.2
Release:          1%{?dist}
Summary:          Quality Control Charts

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-MASS 

BuildRequires:    R-devel tex(latex) R-MASS 

%description
Shewhart quality control charts for continuous, attribute and count data.
Cusum and EWMA charts. Operating characteristic curves.  Process
capability analysis. Pareto chart and cause-and-effect chart. Multivariate
control charts.

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
%doc %{rlibdir}/qcc/html
%doc %{rlibdir}/qcc/doc
%doc %{rlibdir}/qcc/DESCRIPTION
%doc %{rlibdir}/qcc/CITATION
%doc %{rlibdir}/qcc/LICENCE
%{rlibdir}/qcc/R
%{rlibdir}/qcc/demo
%{rlibdir}/qcc/INDEX
%{rlibdir}/qcc/NAMESPACE
%{rlibdir}/qcc/help
%{rlibdir}/qcc/data
%{rlibdir}/qcc/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.2-1
- initial package for Fedora