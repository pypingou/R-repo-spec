%global packname  matrixcalc
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Collection of functions for matrix differential calculus

Group:            Applications/Engineering 
License:          GPL (>=2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
A collection of functions to support matrix differential calculus as
presented in Magnus and Neudecker (1999) Matrix Differential Calculus with
Applications in Statistics and Econometrics, Second Edition, John Wiley,
New York.  Some of the functions are comparable to APL and J functions
which are useful for actuarial models and calculations. This package is
used for teaching and research purposes at the Department of Finance and
Risk Engineering, Polytechnic University, Brooklyn, NY 11201.

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
%doc %{rlibdir}/matrixcalc/html
%doc %{rlibdir}/matrixcalc/DESCRIPTION
%{rlibdir}/matrixcalc/R
%{rlibdir}/matrixcalc/Meta
%{rlibdir}/matrixcalc/help
%{rlibdir}/matrixcalc/INDEX
%{rlibdir}/matrixcalc/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora