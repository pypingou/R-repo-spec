%global packname  rplotengine
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          R as a plotting engine

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-xtable 

BuildRequires:    R-devel tex(latex) R-xtable 

%description
This package is intended for using R as a plotting engine by custom
applications, from a small script launched from the system console, or
even within the R console. The graph parameters are written in an ASCII
text file, which name is passed to the function. The user can choose the
titles, type of the graph, the output formats, proportion of the X-axis
and Y-axis, position of the legend, wether to show or not a grid at the
background, etc. On the other hand, the necessary data must be written in
one or more text files column separated. Optionally, the data files could
include data columns for showing confidence intervals.

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
%doc %{rlibdir}/rplotengine/LICENCE
%doc %{rlibdir}/rplotengine/DESCRIPTION
%doc %{rlibdir}/rplotengine/html
%{rlibdir}/rplotengine/INDEX
%{rlibdir}/rplotengine/help
%{rlibdir}/rplotengine/LICENSE
%{rlibdir}/rplotengine/mygraph.arg
%{rlibdir}/rplotengine/mydata.txt
%{rlibdir}/rplotengine/R
%{rlibdir}/rplotengine/Meta
%{rlibdir}/rplotengine/NAMESPACE

%changelog
* Tue Dec 06 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora