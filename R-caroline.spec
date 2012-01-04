%global packname  caroline
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.6.0
Release:          1%{?dist}
Summary:          A Collection of Database, Data Structure, Visualization and Utility Functions for R

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
The caroline R library contains dozens of functions useful for: database
migration (dbWriteTable2), database style joins & aggregation (nerge,
groupBy & bestBy), data structure conversion (nv, tab2df), legend table
making (sstable & leghead), plot annotation (labsegs & mvlabs), data
visualization (violins, pies & raPlot), character string manipulation (m &
pad), file I/O (write.delim), batch scripting (cmdArgsToVariables) and
many more.  The package's greatest contributions lie in the database style
merge, aggregation and interface functions as well as in it's extensive
use and propagation of row, column and vector names in most functions.

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
%doc %{rlibdir}/caroline/html
%doc %{rlibdir}/caroline/DESCRIPTION
%{rlibdir}/caroline/R
%{rlibdir}/caroline/NAMESPACE
%{rlibdir}/caroline/LICENSE
%{rlibdir}/caroline/INDEX
%{rlibdir}/caroline/Meta
%{rlibdir}/caroline/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6.0-1
- initial package for Fedora