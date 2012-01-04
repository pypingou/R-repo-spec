%global packname  prob
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.2
Release:          1%{?dist}
Summary:          Elementary Probability on Finite Sample Spaces

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package provides a framework for performing elementary probability
calculations on finite sample spaces, which may be represented by data
frames or lists. Functionality includes setting up sample spaces, counting
tools, defining probability spaces, performing set algebra, calculating
probability and conditional probability, tools for simulation and checking
the law of large numbers, adding random variables, and finding marginal
distributions. Characteristic functions for all base R distributions are

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
%doc %{rlibdir}/prob/doc
%doc %{rlibdir}/prob/html
%doc %{rlibdir}/prob/DESCRIPTION
%{rlibdir}/prob/help
%{rlibdir}/prob/Meta
%{rlibdir}/prob/LICENSE
%{rlibdir}/prob/R
%{rlibdir}/prob/NAMESPACE
%{rlibdir}/prob/INDEX

%changelog
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.2-1
- initial package for Fedora