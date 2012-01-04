%global packname  accuracy
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.35
Release:          1%{?dist}
Summary:          Tools for testing and improving accuracy of statistical results.

Group:            Applications/Engineering 
License:          AGPL-3 + file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This is a suite of tools designed to test and improve the accuracy of
statistical computation, including: Summarization of the sensitivity of
linear and non-linear models (lm, glm, mle, nls) to measurement and
numerical error; Sensitivity analysis of dozens of models as run through
Zelig; A generalized cholesky method for correcting non-invertable
Hessians; Tests for the global optimality of non-linear regression and
maximum likelihood results; Tools for obtaining true random numbers using
entropy collected from the system and/or entropy servers on the internet;
A method for converting floating point numbers to normalized fractions;
Benchmark data for checking the accuracy of basic distribution functions.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.35-1
- initial package for Fedora