%global packname  GrapheR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.9.65
Release:          1%{?dist}
Summary:          A multiplatform GUI for drawing customizable graphs in R

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.9-65.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-tcltk 

BuildRequires:    R-devel tex(latex) R-tcltk 

%description
GrapheR is a multiplatform user interface for drawing highly customizable
graphs in R. It aims to be a valuable help to quickly draw publishable
graphs without any knowledge of R commands. Six kinds of graph are
available: histogram, box-and-whisker plot, bar plot, pie chart, curve and
scatter plot.

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
%doc %{rlibdir}/GrapheR/doc
%doc %{rlibdir}/GrapheR/html
%doc %{rlibdir}/GrapheR/DESCRIPTION
%{rlibdir}/GrapheR/data
%{rlibdir}/GrapheR/Meta
%{rlibdir}/GrapheR/lang
%{rlibdir}/GrapheR/R
%{rlibdir}/GrapheR/NAMESPACE
%{rlibdir}/GrapheR/INDEX
%{rlibdir}/GrapheR/help
%{rlibdir}/GrapheR/images

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.9.65-1
- initial package for Fedora