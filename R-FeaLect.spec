%global packname  FeaLect
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.3
Release:          1%{?dist}
Summary:          Scores features for Feature seLection

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-lars R-rms 


BuildRequires:    R-devel tex(latex) R-lars R-rms



%description
For each feature, a score is computed that can be useful for feature
selection. Several random subsets are sampled from the input data and for
each random subset, various linear models are fitted using lars method. A
score is assigned to each feature based on the tendency of LASSO in
including that feature in the models.Finally, the average score and the
models are returned as the output. The features with relatively low scores
are recommended to be ignored because they can lead to overfitting of the
model to the training data. Moreover, for each random subset, the best set
of features in terms of global error is returned. They are useful for
applying Bolasso, the alternative feature selection method that recommends
the intersection of features subsets.

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
%doc %{rlibdir}/FeaLect/html
%doc %{rlibdir}/FeaLect/DESCRIPTION
%doc %{rlibdir}/FeaLect/doc
%{rlibdir}/FeaLect/help
%{rlibdir}/FeaLect/data
%{rlibdir}/FeaLect/NAMESPACE
%{rlibdir}/FeaLect/Meta
%{rlibdir}/FeaLect/INDEX
%{rlibdir}/FeaLect/R

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3-1
- initial package for Fedora