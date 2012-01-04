%global packname  FuncMap
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Hive Plots of R Package Function Calls

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core


Requires:         R-grid R-mvbutils 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-grid R-mvbutils 


%description
FuncMap analyzes the function calls in an R package and creates a hive
plot of the calls, dividing them among functions that only make outgoing
calls (sources), functions that have only incoming calls (sinks), and
those that have both incoming calls and make outgoing calls (managers). 
Function calls can be mapped by their absolute numbers, their normalized
absolute numbers, or their rank.  FuncMap should be useful for comparing
packages at a high level for their overall design.  Plus, it's just plain
fun.  The hive plot concept was developed by Martin Krzywinski
(www.hiveplot.com) and inspired this package.

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
%doc %{rlibdir}/FuncMap/html
%doc %{rlibdir}/FuncMap/NEWS
%doc %{rlibdir}/FuncMap/CITATION
%doc %{rlibdir}/FuncMap/DESCRIPTION
%{rlibdir}/FuncMap/help
%{rlibdir}/FuncMap/R
%{rlibdir}/FuncMap/NAMESPACE
%{rlibdir}/FuncMap/INDEX
%{rlibdir}/FuncMap/Meta

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora