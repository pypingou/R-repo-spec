%global packname  bootruin
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.254
Release:          1%{?dist}
Summary:          A bootstrap test for the probability of ruin in the classical risk process

Group:            Applications/Engineering 
License:          AGPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-254.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package provides a framework for testing the probability of ruin in
the classical (compound Poisson) risk process. It also includes some
procedures for assessing and comparing the performance between the
bootstrap test and the test using asymptotic normality.

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
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.254-1
- initial package for Fedora