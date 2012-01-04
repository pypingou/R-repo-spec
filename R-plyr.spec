%global packname  plyr
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.6
Release:          1%{?dist}
Summary:          Tools for splitting, applying and combining data

Group:            Applications/Engineering 
License:          MIT
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-itertools R-iterators 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-itertools R-iterators 


%description
plyr is a set of tools that solves a common set of problems: you need to
break a big problem down into manageable pieces, operate on each pieces
and then put all the pieces back together.  For example, you might want to
fit a model to each spatial location or time point in your study,
summarise data by panels or collapse high-dimensional arrays to simpler
summary statistics. The development of plyr has been generously supported
by BD (Becton Dickinson).

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
%doc %{rlibdir}/plyr/DESCRIPTION
%doc %{rlibdir}/plyr/CITATION
%doc %{rlibdir}/plyr/html
%doc %{rlibdir}/plyr/NEWS
%{rlibdir}/plyr/INDEX
%{rlibdir}/plyr/tests
%{rlibdir}/plyr/help
%{rlibdir}/plyr/NAMESPACE
%{rlibdir}/plyr/R
%{rlibdir}/plyr/libs
%{rlibdir}/plyr/Meta
%{rlibdir}/plyr/data

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6-1
- initial package for Fedora