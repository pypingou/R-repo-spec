%global packname  adk
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Anderson-Darling K-Sample Test and Combinations of Such Tests

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
The Anderson-Darling K-sample test can be used to test whether several
independent random samples of various sizes come from the same but
unspecified continuous distribution. It is a rank test and consistent
against all alternatives. A low to moderate number of tied observations
can be tolerated. The combination of such tests can be used to test
whether M groups of samples (with K allowed to vary from group to group)
come from respective common distributions, which may vary from group to
group. This is useful in testing for treatment effects in randomized
(incomplete) block designs or in examining whether several laboratories
perform equally well when asked to measure a sufficient number of test
speciments from different batches or materials.

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
%doc %{rlibdir}/adk/NEWS
%doc %{rlibdir}/adk/html
%doc %{rlibdir}/adk/DESCRIPTION
%{rlibdir}/adk/Meta
%{rlibdir}/adk/INDEX
%{rlibdir}/adk/R
%{rlibdir}/adk/NAMESPACE
%{rlibdir}/adk/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.2-1
- initial package for Fedora