%global packname  zipfR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.6.5
Release:          1%{?dist}
Summary:          Statistical models for word frequency distributions

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.6-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Statistical models and utilities for the analysis of word frequency
distributions. The utilities include functions for loading, manipulating
and visualizing word frequency data and vocabulary growth curves.  The
package also implements several statistical models for the distribution of
word frequencies in a population.  (The name of this library derives from
the most famous word frequency distribution, Zipf's law.)

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
%doc %{rlibdir}/zipfR/html
%doc %{rlibdir}/zipfR/DESCRIPTION
%doc %{rlibdir}/zipfR/doc
%{rlibdir}/zipfR/NAMESPACE
%{rlibdir}/zipfR/INDEX
%{rlibdir}/zipfR/help
%{rlibdir}/zipfR/Meta
%{rlibdir}/zipfR/data
%{rlibdir}/zipfR/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6.5-1
- initial package for Fedora