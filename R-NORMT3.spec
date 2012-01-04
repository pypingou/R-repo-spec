%global packname  NORMT3
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Evaluates complex erf, erfc, Faddeeva, and density of sum of Gaussian and Student's t

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Evaluates the probability density function of the sum of the Gaussian and
Student's t density on 3 degrees of freedom. Evaluates the p.d.f. of the
sphered Student's t density function. Also evaluates the erf, and erfc
functions on complex-valued arguments. Thanks to Krishna Myneni the
function is calculates the Faddeeva function also!

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
%doc %{rlibdir}/NORMT3/DESCRIPTION
%doc %{rlibdir}/NORMT3/html
%{rlibdir}/NORMT3/libs
%{rlibdir}/NORMT3/Meta
%{rlibdir}/NORMT3/INDEX
%{rlibdir}/NORMT3/help
%{rlibdir}/NORMT3/NAMESPACE
%{rlibdir}/NORMT3/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.2-1
- initial package for Fedora