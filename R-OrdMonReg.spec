%global packname  OrdMonReg
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Compute least squares estimates of one bounded or two ordered isotonic regression curves

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
We consider the problem of estimating two isotonic regression curves g1*
and g2* under the constraint that they are ordered, i.e. g1* <= g2*. Given
two sets of n data points y_1, ..., y_n and z_1, ..., z_n that are
observed at (the same) deterministic design points x_1, ..., x_n, the
estimates are obtained by minimizing the Least Squares criterion L(a, b) =
sum_{i=1}^n (y_i - a_i)^2 w1(x_i) + sum_{i=1}^n (z_i - b_i)^2 w2(x_i) over
the class of pairs of vectors (a, b) such that a and b are isotonic and
a_i <= b_i for all i = 1, ..., n. We offer two different approaches to
compute the estimates: a projected subgradient algorithm where the
projection is calculated using a PAVA as well as Dykstra's cyclical
projection algorithm.

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
%doc %{rlibdir}/OrdMonReg/DESCRIPTION
%doc %{rlibdir}/OrdMonReg/html
%{rlibdir}/OrdMonReg/NAMESPACE
%{rlibdir}/OrdMonReg/Meta
%{rlibdir}/OrdMonReg/help
%{rlibdir}/OrdMonReg/INDEX
%{rlibdir}/OrdMonReg/data
%{rlibdir}/OrdMonReg/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.2-1
- initial package for Fedora