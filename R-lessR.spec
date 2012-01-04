%global packname  lessR
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.0.2
Release:          1%{?dist}
Summary:          Less Code, More Results

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Each function accomplishes the work of several or more standard R
functions.  For example, two function calls, rad() and full(), together
read the csv data and generate descriptive statistics for all variables in
the data frame, plus histograms and bar charts for all respective
numerical and non-numerical variables. The function smd.t.test introduces
the ODDSMD plot, which displays the Overlapping Density Distributions of
two independent groups as well as a visual display of the mean difference
and standardized mean difference. Other functions provide for descriptive
statistics, the t-test from descriptive statistics, a comprehensive
regression analysis, color plotting, color bar chart, color histogram,
color box plot, density curves, a calibrated power curve plotted with
colors, and the reading and display of csv formatted data. The function
help.me provides a help system that suggests specific analyses and

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
%doc %{rlibdir}/lessR/html
%doc %{rlibdir}/lessR/DESCRIPTION
%{rlibdir}/lessR/Meta
%{rlibdir}/lessR/NAMESPACE
%{rlibdir}/lessR/help
%{rlibdir}/lessR/INDEX
%{rlibdir}/lessR/R

%changelog
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0.2-1
- initial package for Fedora