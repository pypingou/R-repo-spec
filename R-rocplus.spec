%global packname  rocplus
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          ROC, Precision-Recall, Convex Hull and other plots.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-SuppDists 

BuildRequires:    R-devel tex(latex) R-SuppDists 

%description
Creates single and multiple ROC plots, precision-recall, Bayes plots and
others. The plots may be either rough or smooth with confidence limits.
Threshold values, optimum points and other interesting points may be
marked on the plots. The convex hull for multiple curves with blending
fractions for interesting points may be obtained. The axes may have normal
or lognormal scaling.

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
%doc %{rlibdir}/rocplus/html
%doc %{rlibdir}/rocplus/DESCRIPTION
%doc %{rlibdir}/rocplus/doc
%{rlibdir}/rocplus/help
%{rlibdir}/rocplus/R
%{rlibdir}/rocplus/NAMESPACE
%{rlibdir}/rocplus/INDEX
%{rlibdir}/rocplus/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora