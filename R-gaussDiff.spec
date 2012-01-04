%global packname  gaussDiff
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Difference measures for multivariate Gaussian probability density functions

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
A collection difference measures for multivariate Gaussian probability
density functions, such as the Euclidian mean, the Mahalanobis distance,
the Kullback-Leibler divergence, the J-Coefficient, the Minkowski
L2-distance, the Chi-square divergence and the Hellinger Coefficient.

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
%doc %{rlibdir}/gaussDiff/html
%doc %{rlibdir}/gaussDiff/DESCRIPTION
%{rlibdir}/gaussDiff/help
%{rlibdir}/gaussDiff/Meta
%{rlibdir}/gaussDiff/NAMESPACE
%{rlibdir}/gaussDiff/INDEX
%{rlibdir}/gaussDiff/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora