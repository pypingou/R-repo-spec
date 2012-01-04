%global packname  dlm
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.2
Release:          1%{?dist}
Summary:          Bayesian and Likelihood Analysis of Dynamic Linear Models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Maximum likelihood, Kalman filtering and smoothing, and Bayesian analysis
of Normal linear State Space models, also known as Dynamic Linear Models

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
%doc %{rlibdir}/dlm/NEWS
%doc %{rlibdir}/dlm/html
%doc %{rlibdir}/dlm/DESCRIPTION
%doc %{rlibdir}/dlm/doc
%doc %{rlibdir}/dlm/CITATION
%{rlibdir}/dlm/NAMESPACE
%{rlibdir}/dlm/data
%{rlibdir}/dlm/libs
%{rlibdir}/dlm/INDEX
%{rlibdir}/dlm/help
%{rlibdir}/dlm/Meta
%{rlibdir}/dlm/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.2-1
- initial package for Fedora