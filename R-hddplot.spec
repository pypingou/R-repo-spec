%global packname  hddplot
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.54
Release:          1%{?dist}
Summary:          Use known groups in high-dimensional data to derive scores for plots

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS 

BuildRequires:    R-devel tex(latex) R-MASS 

%description
Cross-validated linear discriminant calculations determine the optimum
number of features. Test and training scores from successive
cross-validation steps determine, via a principal components calculation,
a low-dimensional global space onto which test scores are projected, in
order to plot them. Further functions are included that serve didactic

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
%doc %{rlibdir}/hddplot/html
%doc %{rlibdir}/hddplot/DESCRIPTION
%doc %{rlibdir}/hddplot/CITATION
%{rlibdir}/hddplot/help
%{rlibdir}/hddplot/NAMESPACE
%{rlibdir}/hddplot/demo
%{rlibdir}/hddplot/INDEX
%{rlibdir}/hddplot/Meta
%{rlibdir}/hddplot/R
%{rlibdir}/hddplot/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.54-1
- initial package for Fedora