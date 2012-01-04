%global packname  mlbench
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.1.0
Release:          1%{?dist}
Summary:          Machine Learning Benchmark Problems

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.1-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
A collection of artificial and real-world machine learning benchmark
problems, including, e.g., several data sets from the UCI repository.

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
%doc %{rlibdir}/mlbench/html
%doc %{rlibdir}/mlbench/CITATION
%doc %{rlibdir}/mlbench/NEWS
%doc %{rlibdir}/mlbench/DESCRIPTION
%{rlibdir}/mlbench/libs
%{rlibdir}/mlbench/data
%{rlibdir}/mlbench/Meta
%{rlibdir}/mlbench/R
%{rlibdir}/mlbench/help
%{rlibdir}/mlbench/INDEX
%{rlibdir}/mlbench/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.1.0-1
- initial package for Fedora