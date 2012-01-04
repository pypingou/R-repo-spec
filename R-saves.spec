%global packname  saves
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.4
Release:          1%{?dist}
Summary:          Fast load variables

Group:            Applications/Engineering 
License:          AGPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
The purpose of this package is to be able to save and load only the needed
variables/columns of a dataframe in special binary files (tar archives) -
which seems to be a lot faster method than loading the whole binary object
(RData files) via load() function, or than loading columns from
SQLite/MySQL databases via SQL commands (see vignettes). Performance gain
on SSD drives is a lot more sensible compared to basic load() function.
The performance improvement gained by loading only the chosen variables in
binary format can be useful in some special cases (e.g. where merging data
tables is not an option and very different datasets are needed for
reporting), but be sure if using this package that you really need this,
as non-standard file formats are used!

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
%doc %{rlibdir}/saves/html
%doc %{rlibdir}/saves/DESCRIPTION
%doc %{rlibdir}/saves/CITATION
%doc %{rlibdir}/saves/doc
%{rlibdir}/saves/Meta
%{rlibdir}/saves/INDEX
%{rlibdir}/saves/data
%{rlibdir}/saves/NAMESPACE
%{rlibdir}/saves/R
%{rlibdir}/saves/help
RPM build errors:
%{rlibdir}/saves/LICENSE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4-1
- initial package for Fedora