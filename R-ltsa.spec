%global packname  ltsa
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4
Release:          1%{?dist}
Summary:          Linear time series analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Methods of developing linear time series modelling. Methods are given for
loglikelihood computation, forecasting and simulation.

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
%doc %{rlibdir}/ltsa/CITATION
%doc %{rlibdir}/ltsa/doc
%doc %{rlibdir}/ltsa/NEWS
%doc %{rlibdir}/ltsa/DESCRIPTION
%doc %{rlibdir}/ltsa/html
%{rlibdir}/ltsa/R
%{rlibdir}/ltsa/NAMESPACE
%{rlibdir}/ltsa/INDEX
%{rlibdir}/ltsa/help
%{rlibdir}/ltsa/libs
%{rlibdir}/ltsa/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4-1
- initial package for Fedora