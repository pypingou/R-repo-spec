%global packname  microbenchmark
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.3
Release:          1%{?dist}
Summary:          Sub microsecond accurate timing functions.

Group:            Applications/Engineering 
License:          FreeBSD + file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Provides infrastructure to accurately measure and compare the execution
time of R expressions.

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
%doc %{rlibdir}/microbenchmark/DESCRIPTION
%doc %{rlibdir}/microbenchmark/html
%{rlibdir}/microbenchmark/NAMESPACE
%{rlibdir}/microbenchmark/R
%{rlibdir}/microbenchmark/libs
%{rlibdir}/microbenchmark/help
%{rlibdir}/microbenchmark/Meta
%{rlibdir}/microbenchmark/INDEX
%{rlibdir}/microbenchmark/LICENSE

%changelog
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.3-1
- initial package for Fedora