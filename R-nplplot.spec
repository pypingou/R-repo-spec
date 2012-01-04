%global packname  nplplot
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          4.4
Release:          1%{?dist}
Summary:          Plotting non-parametric linkage results

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
nplplot: Plots curves for non parametric linkage results contained within
a file or a table; nplplot.multi: wrapper function for nplplot to graph
multiple plot-data files, and save these in PDF or postscript format;
nplplot.old: the old nplplot function that combined nplplot and
nplplot.multi into one function, please use the other two functions

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
%doc %{rlibdir}/nplplot/DESCRIPTION
%doc %{rlibdir}/nplplot/html
%{rlibdir}/nplplot/Meta
%{rlibdir}/nplplot/INDEX
%{rlibdir}/nplplot/NAMESPACE
%{rlibdir}/nplplot/help
%{rlibdir}/nplplot/data
%{rlibdir}/nplplot/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 4.4-1
- initial package for Fedora